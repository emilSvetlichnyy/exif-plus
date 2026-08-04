/**
 * Local-only EXIF inspect / strip helpers for EXIF+ site tools.
 * Files never leave the browser tab.
 */
(function () {
  const TAG_LABELS = {
    Make: "Camera make",
    Model: "Camera model",
    Software: "Software",
    DateTimeOriginal: "Date taken",
    CreateDate: "Date created",
    ModifyDate: "Date modified",
    LensModel: "Lens",
    ISO: "ISO",
    FNumber: "Aperture",
    ExposureTime: "Shutter",
    FocalLength: "Focal length",
    Artist: "Artist",
    Copyright: "Copyright",
    ImageDescription: "Description",
    Orientation: "Orientation",
    latitude: "Latitude",
    longitude: "Longitude",
  };

  function $(sel, root) {
    return (root || document).querySelector(sel);
  }

  function fmt(value) {
    if (value == null) return "—";
    if (typeof value === "object") {
      try {
        return JSON.stringify(value);
      } catch {
        return String(value);
      }
    }
    return String(value);
  }

  function pickRows(meta) {
    const rows = [];
    const order = Object.keys(TAG_LABELS);
    for (const key of order) {
      if (meta[key] != null && meta[key] !== "") {
        rows.push([TAG_LABELS[key], fmt(meta[key])]);
      }
    }
    if (meta.GPSLatitude != null || meta.latitude != null) {
      /* already covered via latitude/longitude aliases from exifr */
    }
    const extras = [
      "ImageWidth",
      "ImageHeight",
      "ColorSpace",
      "WhiteBalance",
      "Flash",
      "ExposureProgram",
    ];
    for (const key of extras) {
      if (meta[key] != null && !rows.some((r) => r[0] === key)) {
        rows.push([key, fmt(meta[key])]);
      }
    }
    return rows.slice(0, 24);
  }

  async function readMeta(file) {
    if (typeof exifr === "undefined") {
      throw new Error("Metadata reader failed to load. Refresh and try again.");
    }
    const meta = await exifr.parse(file, {
      tiff: true,
      xmp: true,
      icc: false,
      iptc: true,
      gps: true,
      interop: true,
    });
    return meta || {};
  }

  function hasGps(meta) {
    return (
      (meta.latitude != null && meta.longitude != null) ||
      meta.GPSLatitude != null ||
      meta.GPSLongitude != null
    );
  }

  async function stripViaCanvas(file) {
    const url = URL.createObjectURL(file);
    try {
      const img = await new Promise((resolve, reject) => {
        const el = new Image();
        el.onload = () => resolve(el);
        el.onerror = () => reject(new Error("Could not decode this image in the browser."));
        el.src = url;
      });
      const canvas = document.createElement("canvas");
      canvas.width = img.naturalWidth || img.width;
      canvas.height = img.naturalHeight || img.height;
      const ctx = canvas.getContext("2d");
      ctx.drawImage(img, 0, 0);
      const type = file.type === "image/png" ? "image/png" : "image/jpeg";
      const quality = type === "image/jpeg" ? 0.92 : undefined;
      const blob = await new Promise((resolve) => canvas.toBlob(resolve, type, quality));
      if (!blob) throw new Error("Could not export a cleaned image.");
      const base = file.name.replace(/\.[^.]+$/, "") || "photo";
      const ext = type === "image/png" ? "png" : "jpg";
      return new File([blob], `${base}-clean.${ext}`, { type });
    } finally {
      URL.revokeObjectURL(url);
    }
  }

  function downloadFile(file) {
    const href = URL.createObjectURL(file);
    const a = document.createElement("a");
    a.href = href;
    a.download = file.name;
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(href), 1500);
  }

  function renderTable(el, rows) {
    if (!rows.length) {
      el.innerHTML = "<p class=\"note\">No EXIF/IPTC/GPS tags found in this file.</p>";
      return;
    }
    el.innerHTML =
      "<table class=\"meta-table\"><tbody>" +
      rows
        .map(([k, v]) => `<tr><th>${escapeHtml(k)}</th><td>${escapeHtml(v)}</td></tr>`)
        .join("") +
      "</tbody></table>";
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function initTool(root) {
    const mode = root.dataset.mode || "view";
    const input = $(".tool-file", root);
    const zone = $(".dropzone", root);
    const output = $(".tool-output", root);
    const tableHost = $(".meta-host", root);
    const status = $(".tool-status", root);
    const preview = $(".tool-preview", root);
    const downloadBtn = $(".tool-download", root);
    const filenameEl = $(".tool-filename", root);

    let cleanFile = null;
    let previewUrl = null;

    async function handleFile(file) {
      if (!file || !file.type.startsWith("image/")) {
        status.textContent = "Choose a JPEG, PNG, or WebP image.";
        status.className = "tool-status status-warn";
        return;
      }
      status.textContent = "Reading metadata locally…";
      status.className = "tool-status";
      output.classList.add("is-open");
      cleanFile = null;
      if (downloadBtn) downloadBtn.hidden = true;

      try {
        const meta = await readMeta(file);
        const rows = pickRows(meta);
        renderTable(tableHost, rows);
        const gps = hasGps(meta);
        const tagCount = rows.length;

        if (previewUrl) URL.revokeObjectURL(previewUrl);
        previewUrl = URL.createObjectURL(file);
        preview.src = previewUrl;
        preview.alt = "Selected photo preview";
        filenameEl.textContent = file.name;

        if (mode === "view") {
          status.innerHTML = gps
            ? `<span class="status-warn">GPS location found</span> · ${tagCount} tags shown`
            : `<span class="status-ok">No GPS found</span> · ${tagCount} tags shown`;
          return;
        }

        if (mode === "gps" && !gps) {
          status.innerHTML =
            '<span class="status-ok">No GPS to remove</span> · download is optional';
          return;
        }

        status.textContent = "Creating a cleaned copy in your browser…";
        cleanFile = await stripViaCanvas(file);
        if (downloadBtn) {
          downloadBtn.hidden = false;
          downloadBtn.textContent =
            mode === "gps" ? "Download without GPS / EXIF" : "Download cleaned image";
        }
        status.innerHTML =
          '<span class="status-ok">Ready</span> · metadata stripped via local re-encode (HEIC may be unsupported in some browsers)';
      } catch (err) {
        status.textContent = err.message || "Could not process this file.";
        status.className = "tool-status status-danger";
      }
    }

    zone.addEventListener("click", () => input.click());
    zone.addEventListener("dragover", (e) => {
      e.preventDefault();
      zone.classList.add("is-drag");
    });
    zone.addEventListener("dragleave", () => zone.classList.remove("is-drag"));
    zone.addEventListener("drop", (e) => {
      e.preventDefault();
      zone.classList.remove("is-drag");
      const file = e.dataTransfer.files && e.dataTransfer.files[0];
      if (file) handleFile(file);
    });
    input.addEventListener("change", () => {
      const file = input.files && input.files[0];
      if (file) handleFile(file);
    });
    if (downloadBtn) {
      downloadBtn.addEventListener("click", () => {
        if (cleanFile) downloadFile(cleanFile);
      });
    }
  }

  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("[data-exif-tool]").forEach(initTool);
  });
})();

function uploadImage() {
  const input = document.getElementById("imageInput");
  const preview = document.getElementById("previewImage");
  const verdict = document.getElementById("verdict");
  const confidence = document.getElementById("confidence");
  const usage = document.getElementById("usageMessage");
  const resultPanel = document.getElementById("resultPanel");

  if (!input.files.length) {
    alert("Please upload an image!");
    return;
  }

  const file = input.files[0];
  preview.src = URL.createObjectURL(file);
  preview.style.display = "block";

  const formData = new FormData();
  formData.append("image", file);

  fetch("http://127.0.0.1:8000/predict", {
    method: "POST",
    body: formData
  })
  .then(res => res.json())
  .then(data => {

    // Reset glow
    resultPanel.classList.remove("fresh-glow", "half-glow", "spoiled-glow");

    // Restart animation
    verdict.style.animation = "none";
    verdict.offsetHeight;
    verdict.style.animation = null;

    verdict.innerText = data.prediction;
    confidence.innerText = `Confidence: ${data.confidence}%`;

    if (data.prediction === "Fresh") {
      resultPanel.classList.add("fresh-glow");
      usage.innerText = "✅ Safe for consumption.";
    }
    else if (data.prediction === "Half Spoiled") {
      resultPanel.classList.add("half-glow");
      usage.innerText = "⚠️ Consume only after thorough cooking.";
    }
    else {
      resultPanel.classList.add("spoiled-glow");
      usage.innerText = "❌ Unsafe. Dispose immediately.";
    }
  });
}

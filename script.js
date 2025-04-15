document.querySelectorAll("[style]").forEach((el) => {
    el.style.cssText = el.style.cssText.replace(/(\d+)px/g, (_, px) => `${(px / window.innerWidth) * 100}vw`);
});

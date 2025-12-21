
document.addEventListener("DOMContentLoaded", function () {
    const atroposInstances = [
        '.my-atropos',
        '.my-delibery',
        '.my-promocion',
        '.my-servicio'
    ];

    atroposInstances.forEach(selector => {
        Atropos({
            el: selector,
            activeOffset: 50,
            shadow: true,
            shadowScale: 1.05,
            onEnter() {
                console.log(`Enter ${selector}`);
            },
            onLeave() {
                console.log(`Leave ${selector}`);
            },
            onRotate(x, y) {
                console.log(`Rotate ${selector}`, x, y);
            },
        });
    });
});


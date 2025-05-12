import Alpine from "alpinejs";

const bubbleControl = () => ({
    open: false,
    minimized: false,
    showSpeech: true,
});

Alpine.data("bubbleControl", bubbleControl)

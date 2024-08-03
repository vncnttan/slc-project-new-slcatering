<script lang="ts">
    // Random word generator, infinite loop;
    import {onMount} from "svelte";

    export let texts = [""];
    export let speed = 100;
    export let delay = 3000;


    let shown = "";
    let wordObjective = "";
    let isTyping = true;
    let isDeleting = false;

    function getDifferentRandomWord(initialWord: string) {
        let wordIdx = -1;
        do {
            wordIdx = Math.floor(Math.random() * texts.length);
        } while (texts[wordIdx] === initialWord);

        return texts[wordIdx];
    }

    function update() {
        wordObjective = getDifferentRandomWord("");
        setInterval(() => {
            if (isTyping) {
                shown += wordObjective[shown.length]; // Add next character
                if (shown.length === wordObjective.length) {
                    isTyping = false;
                    setTimeout(() => {
                        isDeleting = true;
                    }, delay);
                }
            }

            if (isDeleting) {
                shown = shown.substring(0, shown.length - 1); // Remove last character
                if (shown.length === 0) {
                    isDeleting = false;
                    wordObjective = getDifferentRandomWord(wordObjective);
                    isTyping = true;
                }
            }

        }, speed);
    }

    onMount(update);
</script>

<div class="inline-flex flex-row place-items-center text-orange-sig font-semibold">
    <span>
        {shown}
    </span>
    <span class="input-cursor"></span>
</div>


<style>
    .input-cursor {
        display: inline-block;
        width: 2px;
        height: 1em;
        background-color: black;
        margin-left: 3px;
        animation: blink .6s linear infinite alternate;
    }
    @keyframes blink {
        0% {opacity: 1;}
        40% {opacity: 1;}
        60% {opacity: 0;}
        100% {opacity: 0;}
    }
</style>
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

    function getDifferentRandomWord(initialWord: string){
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

<span>
    {shown}
</span>

<script lang="ts">
    export let value: string;
    export let loading: boolean = false;

    let button: HTMLButtonElement | null = null;

    $: if(!loading && button) {
        button.disabled = false;
        button.classList.remove("opacity-50")
    } else if (loading && button) {
        button.disabled = true;
        button.classList.add("opacity-50")
    }
</script>

<button bind:this={button} type="submit" class="bg-red-sig p-2 text-white">
    {value}
</button>
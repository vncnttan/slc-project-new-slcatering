<script>
    import "../app.css";
    import {SvelteToast} from "@zerodevx/svelte-toast";

    const options = {
        duration: 4000,
        initial: 1,
        next: 0,
        pausable: false,
        dismissable: true,
        reversed: false,
        intro: { x: 256 },
        classes: []
    }
</script>

<SvelteToast {options}/>
<slot />
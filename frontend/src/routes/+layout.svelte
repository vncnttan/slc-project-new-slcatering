<script>
    import "../app.css";
    import {SvelteToast} from "@zerodevx/svelte-toast";
    import {page} from "$app/stores";

    const options = {
        duration: 4000,
        initial: 1,
        next: 0,
        pausable: false,
        dismissable: true,
        reversed: false,
        intro: {x: 256},
        classes: []
    }

    const appName = "slcatering";
    $: title = [appName, ...$page.url.pathname.split("/").slice(1).map(segment => segment.charAt(0).toUpperCase() + segment.slice(1))]
        .filter(Boolean).join(" - ");
</script>

<svelte:head>
    <title>{title}</title>
</svelte:head>

<SvelteToast {options}/>
<slot/>
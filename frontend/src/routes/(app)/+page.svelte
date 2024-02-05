<script>
    import Typewriter from "../../components/Typewriter.svelte";
</script>

<h1 class="text-3xl">Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>

<div>
    <span>
        Typewriter:
        Mau makan apa hari ini?
    </span>
    <Typewriter texts={["Budi 🤤", "Nasi Bakar", "Ayam Goreng", "Nasi Hainam", "Burger", "Bakpao"]} />
</div>

<a href="/login">Login</a>

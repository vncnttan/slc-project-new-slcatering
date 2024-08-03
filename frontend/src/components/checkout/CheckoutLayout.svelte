<script>
    import ProgressBar from "./ProgressBar.svelte";
    export let currentStep = 1;
</script>

<div class="bg-red-sig-gradient w-full min-h-screen">
    <div class="w-full h-full min-h-screen bg-layer-cutout pt-[14vh]">
        <div class="w-full h-full bg-white container mx-auto p-4 md:p-16 lg:px-48 rounded-t-xl min-h-[86vh]">
            <div class="container flex flex-col gap-16 font-karla">
                <ProgressBar currentStep={currentStep}/>
                <slot/>
            </div>
        </div>
    </div>
</div>
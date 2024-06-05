<script lang="ts">
    import CreateMenuGeneralForm from "../../../components/merchant/CreateMenuGeneralForm.svelte";
    import CreateMenuVariantForm from "../../../components/merchant/CreateMenuVariantForm.svelte";
    import ThumbnailForm from "../../../components/merchant/ThumbnailForm.svelte";
    import type {MenuInformationType} from "../../../scripts/helpers";



    let menuInformation: MenuInformationType = {
        thumbnail: "",
        name: "",
        date: "",
        stock: "",
        price: "",
        variants: [],
    }

</script>

<div class="flex flex-col mx-4 !mt-10 gap-12 responsive-container bg-gray-custom p-8 rounded-2xl">
    <div class="text-4xl text-black font-bold">
        Schedule Catering
    </div>
    <div class="flex flex-col gap-6">
        <div class="bg-white  rounded-md flex flex-col gap-4">
            <div class="font-bold">
                Thumbnail
            </div>
            <ThumbnailForm/>
        </div>
        <div class="bg-white  rounded-md flex flex-col gap-4">
            <div class="font-bold">
                General
            </div>
            <CreateMenuGeneralForm menuInformation={menuInformation}/>
        </div>
        <div class="bg-white  rounded-md flex flex-col gap-4">
            <div class="font-bold">
                Variant
            </div>
            <CreateMenuVariantForm menuInformation={menuInformation}/>
        </div>
        <button on:click={() => console.log(menuInformation)}
                class="text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm w-full sm:w-fit px-5 py-3 text-center red-700 red-800">
            Create Menu
        </button>
    </div>
</div>
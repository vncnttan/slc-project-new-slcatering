<script lang="ts">
    import CreateMenuGeneralForm from "../../../components/merchant/CreateMenuGeneralForm.svelte";
    import CreateMenuVariantForm from "../../../components/merchant/CreateMenuVariantForm.svelte";
    import ThumbnailForm from "../../../components/merchant/ThumbnailForm.svelte";
    import {type MenuInformationType, showToast, TOAST_TYPE} from "../../../scripts/helpers";
    import {createMenu} from "../../../scripts/datas/catering-mutations-and-queries";
    import {uploadFile} from "../../../scripts/firebase_upload";

    let menuInformation: MenuInformationType = {
        thumbnail: "",
        name: "",
        date: "",
        stock: "",
        price: "",
        variants: [],
    }

    let menuImageFile: { image: File | null} = {
        image: null
    };

    async function submitSchedulCateringForm() {
        if (menuInformation.name === "" ||
            menuInformation.date === "" ||
            menuInformation.stock === "" ||
            menuInformation.price === ""
        ) {
            showToast("All field is required", TOAST_TYPE.WARNING)
            return
        }

        if (menuInformation.date < new Date().toISOString().split('T')[0]) {
            showToast("Date must be greater than today", TOAST_TYPE.WARNING)
            return
        }

        if (menuImageFile.image === null) {
            showToast("Thumbnail is required", TOAST_TYPE.WARNING)
            return
        }
        menuInformation.thumbnail = await uploadFile(`/${menuInformation.date}/`, menuInformation.name, menuImageFile.image)

        await createMenu(menuInformation)
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
            <ThumbnailForm menuImageFile={menuImageFile}/>
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
        <button on:click={submitSchedulCateringForm}
                class="text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm w-full sm:w-fit px-5 py-3 text-center red-700 red-800">
            Create Menu
        </button>
    </div>
</div>
<script lang="ts">
    import CreateMenuGeneralForm from "../../../components/merchant/CreateMenuGeneralForm.svelte";
    import CreateMenuVariantForm from "../../../components/merchant/CreateMenuVariantForm.svelte";
    import ThumbnailForm from "../../../components/merchant/ThumbnailForm.svelte";
    import { showToast, TOAST_TYPE} from "../../../scripts/helpers";
    import {createMenu} from "../../../scripts/datas/catering-mutations-and-queries";
    import {uploadFile} from "../../../scripts/firebase_upload";
    import type {PageData} from "./$types";
    import {goto} from "$app/navigation";
    import type {MenuInformationType} from "../../../scripts/custom-type-declarations";

    export let data: PageData;

    let menuInformation: MenuInformationType = {
        imageLink: "",
        title: "",
        date: "",
        stock: "",
        price: "",
        catering_variants: [],
    }

    let menuImageFile: { image: File | null} = {
        image: null
    };

    async function submitSchedulCateringForm() {
        if (menuInformation.title === "" ||
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
        menuInformation.imageLink = await uploadFile(`/${menuInformation.date}/`, menuInformation.title, menuImageFile.image)

        try {
            if (data.user === null) {
                showToast("You must login first", TOAST_TYPE.ERROR)
                return
            }
            await createMenu(menuInformation, data.user?.token)
            showToast("Menu created successfully", TOAST_TYPE.SUCCESS)
            await goto('/')
        } catch (e) {
            showToast("Failed to create menu", TOAST_TYPE.ERROR)
        }
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
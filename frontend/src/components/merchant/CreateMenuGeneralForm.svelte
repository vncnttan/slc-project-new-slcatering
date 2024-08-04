<script lang="ts">
    import type {MenuInformationType} from "../../scripts/custom-type-declarations";

    export let menuInformation: MenuInformationType;

</script>

<div class="w-full mx-auto">
    <div class="relative z-0 w-full mb-5 group">
        <input type="text" name="floating_name" id="floating_name" bind:value={menuInformation.title}
               class="block py-2.5 px-0 w-full text-base text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-red-600 peer"
               placeholder="" required/>
        <label for="floating_name"
               class="peer-focus:font-medium absolute text-sm text-gray-500 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-red-600 peer-focus:500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">
            Menu Name
        </label>
    </div>
    <div class="grid md:grid-cols-3 md:gap-6">
        <div class="relative z-0 w-full mb-2 group">
            <input type="date" name="floating_first_name" id="floating_first_name" bind:value={menuInformation.date}
                   class="block py-2.5 px-0 w-full text-base text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-red-600 peer"
                   placeholder=" " required/>
            <label for="floating_first_name"
                   class="peer-focus:font-medium absolute text-sm text-gray-500 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-red-600 peer-focus:500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">
                Date
            </label>

        </div>
        <div class="relative z-0 w-full mb-2 group mt-4 md:mt-0 md:me-4 lg:me-12">
            <input type="number" name="floating_first_name" id="floating_first_name" min="0" bind:value={menuInformation.stock}
                   class="block py-2.5 px-0 w-full text-base text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-red-600 peer"
                   placeholder=" " required/>
            <label for="floating_first_name"
                   class="peer-focus:font-medium absolute text-sm text-gray-500 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-red-600 peer-focus:500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">
                Stock
            </label>
        </div>
        <div class="flex flex-row gap-2 place-items-center mb-2 mt-4 md:mt-0">
            <div class="flex items-center pointer-events-none">
                Rp.
            </div>
            <div class="relative z-0 w-full group">
                <input type="number" name="floating_last_name" id="floating_last_name" min="0" bind:value={menuInformation.price}
                       class="block py-2.5 px-0 w-full text-base text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-red-600 peer"
                       placeholder=" " required/>
                <label for="floating_last_name"
                       class="peer-focus:font-medium absolute text-sm text-gray-500 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 peer-focus:text-red-600 peer-focus:500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">
                    Base Price
                </label>
            </div>
        </div>
    </div>
    <div class="text-sm text-gray-500 mb-5">
        * Catering will not be closed automatically, close order manually on product detail
    </div>
</div>

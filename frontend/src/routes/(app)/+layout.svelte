<!--Navbar Here-->
<script>
    import Typewriter from "../../components/Typewriter.svelte";
    import slcatering_logo from "$lib/assets/slcatering_logo.png";
</script>

<div class="font-inter fixed w-full">
    <div class="py-2 px-10 grid grid-cols-3 w-full h-24">
        <div>
            <img src="{slcatering_logo}" alt="SLCatering Logo" class="h-24 w-64 object-cover"/>
        </div>
        <div class="flex flex-row justify-center place-items-center font-karla">
            <div class="flex flex-row h-fit place-items-center bg-gray-300 rounded-full text-lg">
                <div class="w-64 rounded-full bg-orange-sig text-white h-full text-center p-3">
                    Home
                </div>
                <div class="w-64 rounded-full text-black h-full text-center p-3">
                    History
                </div>
            </div>
        </div>
        <div class="flex flex-col justify-center place-items-end">
            <span class="text-xl font-extrabold">
                NJ23-1
            </span>
            <div class="flex flex-row gap-1">
                <span>
                    Mau makan apa hari ini?
                </span>
                <Typewriter texts={["Budi 🤤", "Nasi Bakar", "Ayam Goreng", "Nasi Hainam", "Burger", "Bakpao"]}/>
            </div>
        </div>
    </div>
</div>


<slot/>
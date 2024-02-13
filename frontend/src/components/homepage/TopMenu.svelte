<script lang="ts">

    let menus = [
        {
            name: "Mango Tea",
            date: "17 November 2023",
            quantity: 24
        },
        {
            name: "Nasi Goreng",
            date: "13 Desember 2023",
            quantity: 20
        },
        {
            name: "Ayam Bakar",
            date: "13 Desember 2023",
            quantity: 20
        },
        {
            name: "Sate Ayam",
            date: "13 Desember 2023",
            quantity: 20
        },
        {
            name: "Sate Kambing",
            date: "13 Desember 2023",
            quantity: 20
        }
    ]
</script>

<div class="grid-rows-5 grid h-full w-full">
    {#each menus as menu, i}
        <div class="{ i === 0 ? 'bg-first-place' :
                i === 1 ? 'bg-second-place' :
                i === 2 ? 'bg-third-place' : '' } py-3 px-6 flex flex-row justify-between">
            <div class="flex flex-col justify-center">
                <div class="text-2xl font-inter font-bold">
                    {menu.name}
                </div>
                <div class="text-xs font-inter text-gray-600 font-semibold">
                    {menu.date}
                </div>
            </div>
            <div class="text-sm font-inter text-black font-semibold flex justify-center place-items-center">
                {menu.quantity} Pcs
            </div>
        </div>
    {/each}
</div>
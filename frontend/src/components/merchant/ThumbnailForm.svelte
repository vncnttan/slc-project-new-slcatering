<script lang="ts">
    let chosenImageLink: string | ArrayBuffer | null;
    let fileInput: HTMLInputElement;

    const onFileSelected = (event: Event) => {
        const target = event.target as HTMLInputElement;
        const files = target.files;

        if (!files || files.length === 0) {
            return; // Handle no file selected case
        }

        const image = files[0];
        const reader = new FileReader();
        reader.readAsDataURL(image);
        reader.onload = (e) => {
            if (e.target && typeof e.target.result === 'string') {
                chosenImageLink = e.target.result;
            } else {
                console.warn('Failed to read file as data URL');
            }
        };
    };
</script>

<div class="w-full mx-auto">
    <input style="display:none" type="file" accept=".jpg, .jpeg, .png" on:change={(e)=>onFileSelected(e)} bind:this={fileInput} >
    <div class="relative z-0 w-full mb-5 group">
        {#if chosenImageLink && typeof chosenImageLink === 'string'}
            <img src={chosenImageLink} alt="Uploaded" class="w-full h-64 object-cover" />
<!--            Create Overlay Gray -->
            <button on:click={()=>{fileInput.click()}} class="absolute top-0 left-0 w-full h-64 bg-black bg-opacity-40"></button>
            <img src={chosenImageLink} alt="Uploaded" class="absolute top-0 left-0 bottom-0 right-0 mx-auto my-auto h-48 w-48 object-cover rounded-md" />
        {:else}
            <button on:click={()=>{fileInput.click()}} class="w-full h-64 border-dashed border-2 flex flex-col gap-2 justify-center place-items-center text-gray-500">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-16">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M6.827 6.175A2.31 2.31 0 0 1 5.186 7.23c-.38.054-.757.112-1.134.175C2.999 7.58 2.25 8.507 2.25 9.574V18a2.25 2.25 0 0 0 2.25 2.25h15A2.25 2.25 0 0 0 21.75 18V9.574c0-1.067-.75-1.994-1.802-2.169a47.865 47.865 0 0 0-1.134-.175 2.31 2.31 0 0 1-1.64-1.055l-.822-1.316a2.192 2.192 0 0 0-1.736-1.039 48.774 48.774 0 0 0-5.232 0 2.192 2.192 0 0 0-1.736 1.039l-.821 1.316Z" />
                    <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 12.75a4.5 4.5 0 1 1-9 0 4.5 4.5 0 0 1 9 0ZM18.75 10.5h.008v.008h-.008V10.5Z" />
                </svg>
                Drop your image here or click to upload
            </button>
        {/if}
    </div>
</div>
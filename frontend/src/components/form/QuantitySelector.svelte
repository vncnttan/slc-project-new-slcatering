<script lang="ts">
    export let inputValue: number;

    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    function validator(node: HTMLInputElement, value: number) {
        return {
            update(value: string) {
                inputValue = inputValue < parseInt(node.min) ? 1 : parseInt(value)
            }
        }
    }
</script>

<div class="relative border border-gray-300 flex flex-row place-items-center px-3 gap-1">
    <input type="number"
           use:validator={inputValue}
           class="w-12 text-gray-900 outline-none text-base rounded-sm focused-text-red-sig block py-1 px-1 dark:bg-gray-700 dark:border-gray-600
                               dark:placeholder-gray-400 dark:text-white "
           required
           max=50
           min=1
           bind:value="{inputValue}"
    />
</div>
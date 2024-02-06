<script>
    import Particle from "../../../components/Particle.svelte";
</script>

<div class="bg-red-sig w-screen h-screen">
    <Particle/>
    <div class="w-full h-full flex justify-center place-items-center">
        <div class="bg-white p-4">
            <div class="flex flex-col gap-2">
                <div class="flex flex-row">
                    <input type="text" name="Username" class="border-2" placeholder="Username"/>
                </div>
                <div class="flex flex-row">
                    <input type="text" name="Username" class="border-2" placeholder="Password"/>
                </div>
                <button>
                    Login
                </button>
            </div>
        </div>
    </div>
</div>

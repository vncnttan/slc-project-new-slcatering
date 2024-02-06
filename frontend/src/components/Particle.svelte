<script lang="ts">
    import {onMount} from "svelte";
    import {ParticleCanvas, Vector} from "../scripts/particle-canvas.js";

    let canvasObj: HTMLCanvasElement | null = null;


    onMount(() => {
        // console.log(canvasObj)
        // Task:
        if(!canvasObj) return;

        canvasObj.width = window.innerWidth
        canvasObj.height = window.innerHeight

        let mousePosition = new Vector(0, 0)
        window.addEventListener("mousemove", function (e) {
            mousePosition.setValue(e.clientX, e.clientY)
        })

        let particleCanvas = new ParticleCanvas(canvasObj, mousePosition)
        particleCanvas.init()
        particleCanvas.draw()
    })
</script>

<div class="h-screen w-screen absolute z-0">
    <canvas bind:this={canvasObj} id="particles-js" class="w-full h-full"></canvas>
</div>
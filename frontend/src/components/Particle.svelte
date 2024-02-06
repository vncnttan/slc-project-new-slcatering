<script lang="ts">
    import {onMount} from "svelte";
    import type {VectorType} from "../../types";

    let canvasObj: HTMLCanvasElement | null = null;

    function Vector(this: VectorType, x: number, y: number){
        this.x = x;
        this.y = y;
    }

    Vector.prototype = {
        add: function(v: VectorType){
            this.x += v.x;
            this.y += v.y;
        },
        sub: function(v: VectorType){
            this.x -= v.x;
            this.y -= v.y;
        },
        mult: function(n: number){
            this.x *= n;
            this.y *= n;
        },
        div: function(n: number){
            this.x /= n;
            this.y /= n;
        },
        mag: function(){
            return Math.sqrt(this.x * this.x + this.y * this.y);
        },
        normalize: function(){
            let m = this.mag();
            if(m !== 0){
                this.div(m);
            }
        }
    }

    onMount(() => {
        console.log(canvasObj)
        // Task:
        //     1. Spawn Circle
        if(!canvasObj) return;
        for (let i = 0; i < 10; i++) {
            let x = Math.random() * canvasObj.width;
            let y = Math.random() * canvasObj.height;
            let r = Math.random() * 10 + 5;
            let color = `rgba(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255}, 1)`;
            let circle = new Path2D();
            circle.arc(x, y, r, 0, 2 * Math.PI);
            let circleObj = {
                x: x,
                y: y,
                r: r,
                color: color,
                path: circle
            }
            let ctx = canvasObj.getContext('2d');
            if(ctx){
                ctx.fillStyle = circleObj.color;
                ctx.fill(circleObj.path);
            }
        }
        //     2. Connect Circle
        //     3. Move Circle
        //     4. Add Interactivity
    })
</script>

<div class="h-full w-full">
    <canvas bind:this={canvasObj} id="particles-js"></canvas>
</div>
// import type {ParticleType, VectorType} from "../../types";
//
// class Vector implements VectorType {
//     constructor(public x: number, public y: number) {
//     }
//
//     static diff(v1: VectorType, v2: VectorType): Vector {
//         return new Vector(v1.x - v2.x, v1.y - v2.y);
//     }
//
//     static add(v1: VectorType, v2: VectorType): Vector {
//         return new Vector(v1.x + v2.x, v1.y + v2.y);
//     }
//
//     add(v: VectorType): void {
//         this.x += v.x;
//         this.y += v.y;
//     }
//
//     magnitude(): number {
//         return Math.sqrt(this.x * this.x + this.y * this.y);
//     }
//
//     mult(n: number): void {
//         this.x *= n;
//         this.y *= n;
//     }
//
//     normalize(): void {
//         const magnitudeVal = this.magnitude();
//         this.x /= magnitudeVal;
//         this.y /= magnitudeVal;
//     }
//
//     setValue(v: VectorType): void {
//         this.x = v.x;
//         this.y = v.y;
//     }
//
//     truncate(max: number): void {
//         const magnitudeVal = this.magnitude();
//         if (magnitudeVal > max) {
//             this.normalize();
//             this.mult(max);
//         }
//     }
//
//     get key(): string {
//         return Math.floor(this.x) + "|" + Math.floor(this.y);
//     }
//
// }
//
// class Particle implements ParticleType {
//     private readonly position: VectorType;
//     private readonly mousePosition: VectorType;
//     private readonly acceleration: VectorType;
//     private readonly maxSpeed: number;
//     private readonly maxForce: number;
//     private readonly velocity: VectorType;
//     private readonly ub: any;
//     private readonly particleMap: any;
//     private readonly chunkSize: any;
//     private readonly radius: number;
//     private readonly radiusLb: number;
//     private readonly radiusUb: number;
//     constructor(position: VectorType, mousePosition: VectorType, ub: any, particleMap: any, chunkSize: any) {
//         this.position = position;
//         this.mousePosition = mousePosition;
//         this.ub = ub;
//         this.particleMap = particleMap;
//         this.chunkSize = chunkSize;
//         this.radius = 1;
//         this.radiusLb = this.radius + 1;
//         this.radiusUb = 2 * (this.radius + 1);
//         this.maxSpeed = .25 * Math.random();
//         this.maxForce = .01;
//         this.velocity = new Vector(20 * Math.random() - 10, 20 * Math.random() - 10);
//         this.acceleration = new Vector(0, 0);
//     }
//
//     update(): void {
//         const desired = Vector.diff(this.mouse, this.position);
//         desired.truncate(this.maxSpeed);
//         const steer = Vector.diff(desired, this.velocity);
//         steer.truncate(this.maxForce);
//         this.acceleration.setValue(steer);
//         this.velocity.add(this.acceleration);
//         this.position.add(this.velocity);
//     }
//
//     clear(): void {
//         this.acceleration.setValue(new Vector(0, 0));
//     }
//
//     draw(ctx: CanvasRenderingContext2D): void {
//         ctx.beginPath();
//         ctx.arc(this.position.x, this.position.y, 4, 0, Math.PI * 2);
//         ctx.fillStyle = "rgba(255, 255, 255, 0.8)";
//         ctx.fill();
//     }
//
//     drawLine(ctx: CanvasRenderingContext2D): void {
//         ctx.beginPath();
//         ctx.moveTo(this.position.x, this.position.y);
//         ctx.lineTo(this.mouse.x, this.mouse.y);
//         ctx.strokeStyle = "rgba(255, 255, 255, 0.3)";
//         ctx.stroke();
//     }
//
//     _getDegInRad(v1: VectorType, v2: VectorType): number {
//         return Math.atan2(v2.y - v1.y, v2.x - v1.x);
//     }
//
//     moveTo(target: VectorType): void {
//         this.mouse.setValue(target);
//     }
// }
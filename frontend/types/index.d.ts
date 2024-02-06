export interface VectorType {
    x: number;
    y: number;
    add: (v: VectorType) => void;
    mult: (n: number) => void;
    setValue: (v: VectorType) => void;
    magnitude: () => number;
    normalize: () => void;
    truncate: (max: number) => void;
    get key(): string;
}

export interface ParticleType {
    position: VectorType;
    velocity: VectorType;
    acceleration: VectorType;
    maxSpeed: number;
    maxForce: number;
    update: () => void;
    clear: () => void;
    draw: (ctx: CanvasRenderingContext2D) => void;
    drawLine: (ctx: CanvasRenderingContext2D) => void;
    _getDegInRad: (v1: VectorType, v2: VectorType) => number;
    moveTo: (target: VectorType) => void;
}
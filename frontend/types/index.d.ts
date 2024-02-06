export interface VectorType {
    x: number;
    y: number;
    add: (v: VectorType) => void;
    sub: (v: VectorType) => void;
    mult: (n: number) => void;
    div: (n: number) => void;
    mag: () => number;
    normalize: () => void;
}
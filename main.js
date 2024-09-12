const wasm = await window.loadManifold();
wasm.setup();

const { Manifold } = wasm;

const box = Manifold.cube([100, 100, 100], true);
const ball = Manifold.sphere(60, 100);
const result = box.subtract(ball);

console.log(result.getMesh());

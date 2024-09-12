#!/usr/bin/env node
import * as esbuild from 'esbuild';

await esbuild.build({
  entryPoints: ['main.js'],
  bundle: true,
  outfile: 'bundle.js',
  format: 'esm',
  sourcemap: true,
});

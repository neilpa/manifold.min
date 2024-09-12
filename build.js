#!/usr/bin/env node
import * as esbuild from 'esbuild';

const context = await esbuild.context({
  entryPoints: ['main.js'],
  bundle: true,
  outfile: 'bundle.js',
  format: 'esm',
  sourcemap: true,
});

// TODO: Log on rebuild
await context.watch();

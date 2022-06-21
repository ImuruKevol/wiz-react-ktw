const esbuild = require("esbuild");
const { sassPlugin } = require("esbuild-sass-plugin");
const args = process.argv.slice(2);

const pluginCache = new Map();
esbuild.build({
  entryPoints: [`${args[0]}`],
  outfile: `${args[1]}`,
  bundle: true,
  loader: {
    ".svg": "dataurl",
    '.png': 'dataurl',
    '.woff': 'dataurl',
    '.woff2': 'dataurl',
    '.eot': 'dataurl',
    '.ttf': 'dataurl',
  },
  plugins: [
    sassPlugin({
      implementation: "node-sass",
      cache: pluginCache,
    }),
  ],
});


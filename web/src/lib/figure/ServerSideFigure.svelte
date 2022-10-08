<script lang="ts">
	import fs from 'fs';

	export let file: string;

	let svg = fs.readFileSync(`static/figures/${file}.svg`, 'utf-8');
	svg = svg.replace(/<svg([^>]*)height="[^"]+" /, '<svg$1');
	svg = svg.replace(/<svg([^>]*)width="[^"]+" /, '<svg$1');
</script>

{@html svg}

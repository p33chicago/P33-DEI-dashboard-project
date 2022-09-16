<script type="ts">
    import Lipsum from "$lib/Lipsum.svelte";
    import {excellence} from "$lib/domain/Indicator.ts";

    export let score: string;
</script>

<h1>{score} {excellence.name}</h1>
<p>
    <Lipsum words="10" />
</p>
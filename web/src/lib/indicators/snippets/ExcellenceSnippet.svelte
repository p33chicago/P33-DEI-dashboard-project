<script type="ts">
    import Lipsum from "../../Lipsum.svelte";
    import {excellence} from "../../domain/Indicator.ts";

    export let score: string;
</script>

<h1>{score} {excellence.name}</h1>
<p>
    <Lipsum words="10" />
</p>
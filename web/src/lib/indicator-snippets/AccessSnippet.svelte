<script type="ts">
    import Lipsum from "$lib/Lipsum.svelte";
    import {access} from "$lib/domain/Indicator.ts";

    export let score: string;
</script>

<h1>{score} {access.name}</h1>
<p>
    <Lipsum words="10" />
</p>
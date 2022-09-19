<script type="ts">
    import Lipsum from "../../Lipsum.svelte";
    import {proficiency} from "../../domain/Indicator.ts";

    export let score: string;
</script>

<h1>{score} {proficiency.name}</h1>
<p>
    <Lipsum words="10" />
</p>
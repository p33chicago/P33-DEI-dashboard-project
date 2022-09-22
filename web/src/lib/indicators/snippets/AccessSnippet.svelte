<script type="ts">
    import Lipsum from "../../Lipsum.svelte";
    import {access} from "../../domain/Indicator.ts";

    export let score: string;
</script>

<h1>{score} {access.name}</h1>
<!-- <p>
    <Lipsum words="10" />
</p> -->
<script type="ts">
    import type {Lifestage} from "$lib/domain/Lifestage";

    export let lifestage: Lifestage;
    export let area: string;
    export let score: number;
</script>
<div class="flex">
    <div>img</div>
    <div class="grow">
        <h1>{lifestage.name}</h1>
        <h2>{area}</h2>
    </div>
    <div>
        {score}
        <hr/>
        100<br/>
        Equity score
    </div>
</div>
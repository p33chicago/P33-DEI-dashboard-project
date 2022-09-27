<script type="ts">
    import Figure from "$lib/figure/Figure.svelte";
    import DataDive from "$lib/DataDive.svelte";
    import {k8} from "$lib/domain/Lifestage.ts";
</script>

<DataDive
        header="4th grade Math Advanced"
        subheader="Percent of CPS 4th graders advanced in math by race/ethnicity"
>
    <svelte:fragment slot="story">
        <p>
            In CPS 4th grade, Asian have the highest proportion of students who excel at math. The proportion is 1.6
            times higher than White, 8 times higher than Hispanics, and 16 times higher than black.
        </p>
        <p>
            The proportion of 4th graders who excelled at math is slightly higher in CPS than the national average
            across all ethnic groups.
        </p>
    </svelte:fragment>
    <svelte:fragment slot="takeaways">
        <p>
            The gap/disparity in ethnic groups is significantly enlarged from proficient students to advanced students.
        </p>
    </svelte:fragment>
    <Figure lifestage={k8.route} name="k4_math_adv" slot="figure"/>
</DataDive>

<DataDive
        header="8th grade Math Advanced"
        subheader="Percent of CPS 8th graders advanced in math by race/ethnicity"
>
    <svelte:fragment slot="story">
        <p>
            In CPS 8th grade, Asian have the highest proportion of students who excel at math. The proportion is 1.7
            times higher than White, 6 times higher than Hispanics, and 19 times higher than black.
        </p>
        <p>
            The proportion of 8th graders who excelled at math is slightly higher in CPS than the national average
            across all ethnic groups.
        </p>
    </svelte:fragment>
    <svelte:fragment slot="takeaways">
        <p>
            The proportion of Hispanic students who excelled at math has increased by 50% from 4th to 8th grade. This
            increment in population is 2.8 times greater than the increment of the other three ethnic groups combined.
        </p>
    </svelte:fragment>
    <Figure lifestage={k8.route} name="math_adv" slot="figure"/>
</DataDive>



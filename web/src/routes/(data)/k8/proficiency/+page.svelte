<script type="ts">
    import Figure from "$lib/figure/Figure.svelte";
    import DataDive from "$lib/DataDive.svelte";
    import {k8} from "$lib/domain/Lifestage.ts";
</script>

<DataDive
        header="4th grade math Proficiency and above"
        subheader="The proportion of CPS 4th graders at or above math proficiency by race/ethnicity"
>
    <svelte:fragment slot="story">
        <p>
            In CPS 4th grade, White students have the highest math proficiency rate,1.1 times higher than Asians, 1.8 times higher than Hispanics, and 2.8 times higher than black.
        </p>
        <p>
            The proportion of math proficient students in 4th grade is noticeably lower in CPS than the national average across all ethnic groups.
        </p>
    </svelte:fragment>
    <svelte:fragment slot="takeaways">
        <p>
            In relation to the national average algebra enrollment rate, White and Asian students are outperforming, while black students are.
        </p>
    </svelte:fragment>
    <!--    <Figure lifestage={k8.route} name="k4_math_profAndAbove" slot="figure"/>-->
</DataDive>

<DataDive
        header="8th grade math Proficiency and above"
        subheader="The proportion of CPS 8th graders at or above math proficiency by race/ethnicity"
>
    <svelte:fragment slot="story">
        <p>
            In CPS 8th grade, Asian and White students have the highest math proficiency rate, 1.6 times higher than Hispanics, and 2.6 times higher than black.
        </p>
        <p>
            In the 8th grade, in relation to the national average, White and Asians have significantly lower math proficiency rates, while that of Black and Hispanics is slightly higher.
        </p>
    </svelte:fragment>
    <svelte:fragment slot="takeaways">
        <p>
            Using the national average as a benchmark, the math proficiency rate of Black and Hispanic students in CPS  improved from 4th to 8th grades.
        </p>
    </svelte:fragment>
    <!--    <Figure lifestage={k8.route} name="math_profAndAbove" slot="figure"/>-->
</DataDive>

<DataDive
        header="8th grade passing algebra"
        subheader="The proportion of CPS 8th graders enrolled in algebra classes passing algebra by race/ethnicity"
>
    <svelte:fragment slot="story">
        <p>
            The algebra passing rate in CPS is greater than 95% across all ethnic groups, significantly higher than the national average.
        </p>
        <p>
            Minor inequality detected in this metric.
        </p>
    </svelte:fragment>
    <svelte:fragment slot="takeaways">
        <p>
            Great performance of CPS algebra class.
        </p>
    </svelte:fragment>
    <!--    <Figure lifestage={k8.route} name="algebra_pass" slot="figure"/>-->
</DataDive>


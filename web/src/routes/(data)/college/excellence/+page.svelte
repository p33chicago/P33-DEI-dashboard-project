<script type="ts">
    // import Figure from "$lib/figure/Figure.svelte";
    import DataDive from "$lib/DataDive.svelte";
    // import {college} from "$lib/domain/Lifestage.ts";
</script>

<DataDive
        header="Illinois CS/Computing Degree Enrollment for Top 3"
        subheader="The proportion of college students enrolled into a CS/Computing degree at a top 3 Illinois university by race/ethnicity"
>
    <svelte:fragment slot="story">
        <p>
            At the University of Chicago, Northwestern University, and the UIC,
            Over 17 out of 100 Asian enroll in a CS program, the ratio is 5 out of 100 for White students,
            4 out of 100 for Hispanic students, and 3 out of 100 for black students.
        </p>
        <p>
            In comparison with Stanford, MIT, and Carnegie Mellon University,
            Illinois’s three top universities have a massive disparity in CS program enrolment rate conferral rates in
        </p>
    </svelte:fragment>

    <svelte:fragment slot="takeaways">
        <p></p>
    </svelte:fragment>
    <!--    <Figure lifestage={college.route} name="topThree_cs_enrol" slot="figure"/>-->
</DataDive>

<DataDive
        header="Illinois CS/Computing Degree Persistence for Top 3"
        subheader="The proportion of college students that enrolled in a top 3 Illinois university and obtained a CS/Computing degree by race/ethnicity"
>
    <svelte:fragment slot="story">
        <p>
            At the University of Chicago, Northwestern University, and the UIC, the number of Black and Hispanic students who obtain a diploma in CS is only 1/5 of the total enrollment in the CS program.
        </p>
        <p>
            In comparison with Stanford, MIT, and Carnegie Mellon University,  three top universities in Illinois have a noticeably lower percentage of CS students who persist and obtain a CS diploma.
        </p>
    </svelte:fragment>

    <svelte:fragment slot="takeaways">
        <p>
            At the University of Chicago, Northwestern University, and the UIC, averaging 1 out of 5 Black and Hispanic students who enrolled in the CS program drop off.
        </p>
    </svelte:fragment>
    <!--    <Figure lifestage={college.route} name="topThree_cs_persist" slot="figure"/>-->
</DataDive>

<DataDive
        header="Illinois CS/Computing Degree Conferral for Top 3"
        subheader="The proportion of degrees conferred by top 3 Illinois institutions that are CS/Computing degrees by race/ethnicity"
>
    <svelte:fragment slot="story">
        <p>
            At the University of Chicago, Northwestern University, and the UIC, Over 16 out of 100 Asian graduates are CS majors, the ratio is 5 out of 100 for Hispanic and white graduates, and 3 out of 100 for black graduates.
        </p>
        <p>
            In comparison with Stanford, MIT, and Carnegie Mellon University, Illinois’s three top universities have a massive disparity in CS degree conferral.
        </p>
    </svelte:fragment>

    <svelte:fragment slot="takeaways">
        <p>
            At the Universities in Illinois, the percentage of Black students who obtained a CS diploma is remarkably lower than that of Hispanic students.
        </p>
    </svelte:fragment>
    <!--    <Figure lifestage={college.route} name="topThree_cs_confer" slot="figure"/>-->
</DataDive>
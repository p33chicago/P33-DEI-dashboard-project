import type {Load} from "@sveltejs/kit";
import type {Scorecard} from "$lib/domain/Scorecard.ts";
import {scorecard} from "$lib/domain/Scorecard.ts";

export const load: Load<{ scorecard: Scorecard }> = async () => {
    return {scorecard}
}
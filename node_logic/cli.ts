import { validateSkill } from "./lib/validate";
import { parseSkillMd } from "./lib/utils";
import { runEval, findProjectRoot } from "./lib/run-eval";
import { improveDescription } from "./lib/improve-description";
import { runLoop } from "./lib/run-loop";
import { generateBenchmark, generateMarkdown } from "./lib/aggregate";
import { generateHtml as generateReportHtml } from "./lib/report";
import { readFileSync, writeFileSync } from "fs";
import { join } from "path";

async function main() {
  const args = process.argv.slice(2);
  const command = args[0];

  try {
    if (command === "validate") {
      const skillPath = args[1];
      const result = validateSkill(skillPath);
      console.log(JSON.stringify(result, null, 2));
    } else if (command === "parse") {
      const skillPath = args[1];
      const meta = parseSkillMd(skillPath);
      console.log(JSON.stringify({
        name: meta.name,
        description: meta.description,
        content: meta.fullContent,
        contentLength: meta.fullContent.length
      }, null, 2));
    } else if (command === "eval") {
      const evalSetPath = args[1];
      const skillPath = args[2];
      const evalSet = JSON.parse(readFileSync(evalSetPath, "utf-8"));
      
      const validation = validateSkill(skillPath);
      if (!validation.valid) throw new Error(`Invalid skill: ${validation.message}`);

      const meta = parseSkillMd(skillPath);
      const result = await runEval({
        evalSet,
        skillName: meta.name,
        description: meta.description,
        numWorkers: 10,
        timeout: 30,
        projectRoot: findProjectRoot(),
        runsPerQuery: 3,
        triggerThreshold: 0.5
      });
      console.log(JSON.stringify(result, null, 2));
    } else if (command === "improve") {
      const skillPath = args[1];
      const evalResultsPath = args[2];
      const meta = parseSkillMd(skillPath);
      const evalResults = JSON.parse(readFileSync(evalResultsPath, "utf-8"));

      const newDescription = await improveDescription({
        skillName: meta.name,
        skillContent: meta.fullContent,
        currentDescription: meta.description,
        evalResults,
        history: [],
        model: undefined,
        logDir: null,
        iteration: null
      });

      console.log(JSON.stringify({ description: newDescription, charCount: newDescription.length }, null, 2));
    } else {
      console.error(JSON.stringify({ error: `Unknown command: ${command}` }));
      process.exit(1);
    }
  } catch (error) {
    if (error instanceof Error) {
        console.error(JSON.stringify({ error: error.message }));
    } else {
        console.error(JSON.stringify({ error: String(error) }));
    }
    process.exit(1);
  }
}

main();

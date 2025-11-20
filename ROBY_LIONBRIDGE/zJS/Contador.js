ACCEPTED JOBS

let input = (document.evaluate('/html/body/ltx-root/div/div[2]/main/lcx-accepted-jobs/lcx-accepted-jobs-list/div/div/ltx-jobs-list/div/div', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue).children.length;
return input;

ACCEPTED JOBS
/html/body/ltx-root/div/div[2]/main/lcx-accepted-jobs/lcx-accepted-jobs-list/div/div/ltx-jobs-list/div/div


AVAILABLE JOBS
    / html / body / ltx - root / div / div[2] / main / app - available - jobs / lcx - available - jobs - list
    / html / body / ltx - root / div / div[2] / main / app - available - jobs / lcx - available - jobs - list / div / div / ltx - jobs - list / div / div

let input = (document.evaluate('/html/body/ltx-root/div/div[2]/main/app-available-jobs/lcx-available-jobs-list/div/div/ltx-jobs-list/div/div', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue).children.length;
return input;


funcional
let element = document.evaluate('/html/body/ltx-root/div/div[2]/main/app-available-jobs/lcx-available-jobs-list/div/div/ltx-jobs-list/div/div', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
return element ? element.children.length : 0;
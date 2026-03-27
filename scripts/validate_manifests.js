const fs = require('fs');
const path = require('path');

function validateManifest(filePath) {
  console.log(`Validating ${filePath}...`);
  if (!fs.existsSync(filePath)) {
    throw new Error(`File not found: ${filePath}`);
  }

  const content = fs.readFileSync(filePath, 'utf8');
  let json;
  try {
    json = JSON.parse(content);
  } catch (e) {
    throw new Error(`Invalid JSON in ${filePath}: ${e.message}`);
  }

  const requiredFields = ['format_version', 'header', 'modules'];
  for (const field of requiredFields) {
    if (!json[field]) {
      throw new Error(`Missing required field '${field}' in ${filePath}`);
    }
  }

  const requiredHeaderFields = ['name', 'description', 'uuid', 'version'];
  for (const field of requiredHeaderFields) {
    if (!json.header[field]) {
      throw new Error(`Missing required field 'header.${field}' in ${filePath}`);
    }
  }

  console.log(`${filePath} is valid.`);
}

try {
  validateManifest(path.join(__dirname, '../behavior_pack/manifest.json'));
  validateManifest(path.join(__dirname, '../resource_pack/manifest.json'));
  console.log('All manifest validations passed!');
} catch (e) {
  console.error(`Validation failed: ${e.message}`);
  process.exit(1);
}

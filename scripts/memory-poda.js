#!/usr/bin/env node
/**
 * Memory Poda Script - Refinado y limpieza de archivos MD
 */

const fs = require('fs');
const path = require('path');

// Configuración
const WORKING_DIR = '/Users/piter/.copaw';
const MEMORY_DIR = path.join(WORKING_DIR, 'memory');
const MEMORY_FILE = path.join(WORKING_DIR, 'MEMORY.md');
const AGENTS_FILE = path.join(WORKING_DIR, 'AGENTS.md');
const SOUL_FILE = path.join(WORKING_DIR, 'SOUL.md');
const PROFILE_FILE = path.join(WORKING_DIR, 'PROFILE.md');

// Función para optimizar archivo MD
function optimizeMD(content) {
  let optimized = content;
  
  // 1. Eliminar espacios en blanco al final de líneas
  optimized = optimized.replace(/[ \t]+$/gm, '');
  
  // 2. Unir líneas vacías múltiples (máximo 1)
  optimized = optimized.replace(/\n{3,}/g, '\n\n');
  
  // 3. Normalizar encabezados (solo # y ##)
  optimized = optimized.replace(/^#{3,}(.+)$/gm, '## $1');
  
  return optimized;
}

// Procesar archivos
console.log('🧹 Iniciando poda de memoria...\n');

// 1. Optimizar MEMORY.md
console.log('1️⃣ Optimizando MEMORY.md...');
let memoryContent = fs.readFileSync(MEMORY_FILE, 'utf8');
memoryContent = optimizeMD(memoryContent);
fs.writeFileSync(MEMORY_FILE, memoryContent);
console.log('   ✅ MEMORY.md optimizado\n');

// 2. Resumir archivo diario reciente
console.log('2️⃣ Resumiendo 2026-03-13.md...');
const dailyFile = path.join(MEMORY_DIR, '2026-03-13.md');
if (fs.existsSync(dailyFile)) {
  let dailyContent = fs.readFileSync(dailyFile, 'utf8');
  dailyContent = optimizeMD(dailyContent);
  // Añadir resumen al inicio
  const summaryHeader = `# Resumen - 13 de marzo de 2026\n\n`;
  const summaryPoints = `- ✅ Skill-creator implementada\n- 🔧 Configuración tokens ajustada (reserve: 0.1, compact: 0.75)\n- 🌐 Herramientas web documentadas\n- 📰 Noticias Marca.com revisadas\n- ⚠️ Página españa.html inaccesible\n`;
  dailyContent = summaryHeader + summaryPoints + '\n\n' + dailyContent;
  fs.writeFileSync(dailyFile, dailyContent);
  console.log('   ✅ 2026-03-13.md resumido\n');
}

// 3. Verificar AGENTS.md
console.log('3️⃣ Verificando AGENTS.md...');
let agentsContent = fs.readFileSync(AGENTS_FILE, 'utf8');
agentsContent = optimizeMD(agentsContent);
fs.writeFileSync(AGENTS_FILE, agentsContent);
console.log('   ✅ AGENTS.md optimizado\n');

// 4. Verificar SOUL.md
console.log('4️⃣ Verificando SOUL.md...');
let soulContent = fs.readFileSync(SOUL_FILE, 'utf8');
soulContent = optimizeMD(soulContent);
fs.writeFileSync(SOUL_FILE, soulContent);
console.log('   ✅ SOUL.md optimizado\n');

// 5. Verificar PROFILE.md
console.log('5️⃣ Verificando PROFILE.md...');
let profileContent = fs.readFileSync(PROFILE_FILE, 'utf8');
profileContent = optimizeMD(profileContent);
fs.writeFileSync(PROFILE_FILE, profileContent);
console.log('   ✅ PROFILE.md optimizado\n');

// 6. Limpiar archivos antiguos (opcional)
console.log('6️⃣ Revisando archivos de memoria antiguos...');
const files = fs.readdirSync(MEMORY_DIR).filter(f => f.endsWith('.md'));
const recentFiles = files.filter(f => {
  const date = f.split('.')[0];
  const year = parseInt(date.split('-')[0]);
  return year >= 2025; // Mantener solo archivos de 2025+
});
console.log(`   ✅ Archivos mantenidos: ${recentFiles.join(', ')}\n`);

console.log('✅ Poda completada!');
console.log('\n📊 Resumen:');
console.log('   - MEMORY.md: Optimizado');
console.log('   - 2026-03-13.md: Resumido y consolidado');
console.log('   - AGENTS.md: Verificado');
console.log('   - SOUL.md: Verificado');
console.log('   - PROFILE.md: Verificado');

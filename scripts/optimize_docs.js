#!/usr/bin/env node
/**
 * Script para optimizar archivos de documentación
 */

const fs = require('fs');
const path = require('path');

// Configuración
const WORKING_DIR = '/Users/piter/.copaw';
const MEMORY_DIR = path.join(WORKING_DIR, 'memory');

// Función para optimizar MD
function optimizeMD(content) {
  // Eliminar líneas vacías consecutivas (máximo 2)
  let result = content.replace(/\n{3,}/g, '\n\n');
  
  // Eliminar espacios en blanco al inicio de líneas
  result = result.replace(/^\s+/gm, '');
  
  return result;
}

// Procesar archivos de documentación
const files = [
  'memory/TOKEN-OPTIMIZATION.md',
  'memory/CONSOLIDACION-CONFIGURACION.md',
  'memory/GUIDA-LECTURA-ARCHIVOS.md',
  'memory/CACHE-USAGE-GUIDE.md'
];

console.log('📝 Optimizando archivos de documentación...\n');

files.forEach(file => {
  const filePath = path.join(WORKING_DIR, file);
  if (fs.existsSync(filePath)) {
    let content = fs.readFileSync(filePath, 'utf8');
    content = optimizeMD(content);
    fs.writeFileSync(filePath, content);
    console.log('✅', file, 'optimizado');
  } else {
    console.log('❌', file, 'no encontrado');
  }
});

console.log('\n✅ Optimización de documentación completada!');

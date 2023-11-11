const isProduction = process.env.NODE_ENV === 'production';

export const apiBase = isProduction ? '' : 'http://127.0.0.1:8001';
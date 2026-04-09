module.exports = {
	root: true,
	extends: [
		'eslint:recommended',
		'plugin:@typescript-eslint/recommended',
		'plugin:svelte/recommended',
		'plugin:cypress/recommended',
		'prettier'
	],
	parser: '@typescript-eslint/parser',
	plugins: ['@typescript-eslint'],
	rules: {
		'no-undef': 'off',
		'no-constant-condition': 'off',
		'no-control-regex': 'off',
		'no-prototype-builtins': 'off',
		'no-async-promise-executor': 'off',
		'getter-return': 'off',
		'prefer-const': 'off',
		'@typescript-eslint/no-explicit-any': 'off',
		'@typescript-eslint/no-unused-vars': 'off',
		'@typescript-eslint/no-unused-expressions': 'off',
		'@typescript-eslint/no-empty-object-type': 'off',
		'@typescript-eslint/no-unsafe-function-type': 'off',
		'@typescript-eslint/ban-ts-comment': 'off',
		'no-empty': 'off',
		'no-ex-assign': 'off',
		'no-unsafe-optional-chaining': 'off',
		'no-useless-escape': 'off',
		'no-extra-boolean-cast': 'off'
	},
	parserOptions: {
		sourceType: 'module',
		ecmaVersion: 2020,
		extraFileExtensions: ['.svelte']
	},
	env: {
		browser: true,
		es2017: true,
		node: true
	},
	overrides: [
		{
			files: ['**/*.svelte'],
			parser: 'svelte-eslint-parser',
			parserOptions: {
				parser: '@typescript-eslint/parser'
			},
			rules: {
				'@typescript-eslint/no-unused-vars': 'off',
				'svelte/no-at-html-tags': 'off',
				'svelte/valid-compile': 'off',
				'svelte/no-unused-svelte-ignore': 'off',
				'svelte/no-inner-declarations': 'off'
			}
		}
	]
};

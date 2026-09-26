import type { Browser, BrowserContext, CDPSession, Page } from 'playwright';

export type Status = 'pass' | 'fail' | 'incomplete' | 'skipped' | 'n/a';
export type CheckResult = { id: string; status: Status; thresholds: Record<string, number>; items: unknown[]; reason?: string | null };
export type RunOptions = {
  input: string; root?: string; width?: number; height?: number; scale: number; at: number | 'end';
  settle: number; boot: number; media: 'screen' | 'print'; waitFor?: string; timeout: number;
  allowNetwork: boolean; simulate?: string; pdf: boolean; strict: boolean; outDir?: string;
  checks?: string[]; thresholds: Record<string, number>;
};
export type Session = { browser: Browser; context: BrowserContext; page: Page; cdp: CDPSession; url: string;
  stop: () => Promise<void>; blocked: { url: string; reason: string }[]; errors: string[]; width: number; height: number; scale: number; svgInput:boolean; allowNetwork:boolean };
export type CheckContext = { session: Session; png: string; pdf?: string; options: RunOptions };
export type Scale = { type: string; domain: number[]; range: number[] };

export const CHECK_IDS = ['resources', 'console', 'fonts', 'overflow', 'collision', 'contrast', 'cvd', 'fidelity', 'a11y', 'value', 'pdf-fonts'];

import type { CheckContext } from '../model.ts';
import { result } from './common.ts';

export async function run(ctx: CheckContext) {
  const items = ctx.session.blocked.map(row => ({ url: row.url, reason: row.reason }));
  return result(ctx, 'resources', items.length ? 'fail' : 'pass', items);
}

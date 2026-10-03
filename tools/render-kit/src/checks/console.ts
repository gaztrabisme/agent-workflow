import type { CheckContext } from '../model.ts';
import { result } from './common.ts';

export async function run(ctx: CheckContext) {
  const items = ctx.session.errors.map(message => ({ message: message.slice(0, 200) }));
  return result(ctx, 'console', items.length ? 'fail' : 'pass', items);
}

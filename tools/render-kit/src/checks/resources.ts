import type { CheckContext } from '../model.ts';
import { expectedRequest, result } from './common.ts';

export async function run(ctx: CheckContext) {
  const items = ctx.session.blocked.map(row => {
    const expected=expectedRequest(row.url,row.reason,ctx.options.expectedRequests);
    return expected?{url:row.url,reason:row.reason,status:'expected',expected_status:expected.status,pattern:expected.pattern}:{url:row.url,reason:row.reason,status:'unexpected'};
  });
  return result(ctx, 'resources', items.some((item:any)=>item.status==='unexpected') ? 'fail' : 'pass', items);
}

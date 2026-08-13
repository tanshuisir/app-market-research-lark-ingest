# 来源与在线状态规则

## Evidence Priority

1. App Store or Google Play product page: primary evidence of current availability in the requested storefront.
2. Qimai: iOS historical metadata and exact removal time.
3. Diandian: Android/Google Play historical metadata and exact removal time; may supplement store data.
4. iTunes Lookup: efficient iOS metadata source, especially for US storefront batch checks.

Use multiple sources when they disagree. Preserve the URLs that make a conclusion traceable.

## Current Status

- Write `在架` when the correct stable ID resolves to a live store product in the target storefront.
- Write `已下架` when the store and a historical source establish removal/unavailability for that same stable ID.
- Write `待核查` when login, source errors, regional ambiguity, or conflicting identity prevents a reliable conclusion.
- A zero-result iTunes Lookup is not sufficient on its own to mark an app removed.
- Qimai text such as `当前应用信息暂时无法提供` is not an exact removal timestamp and must not be converted into one.
- A 404, login wall, rate limit, or transient page failure is source failure, not removal evidence.

## Removal Time

- Prefer an explicit historical timestamp tied to the stable ID, for example `2026年08月06日07点已下架`.
- Normalize that example to `2026-08-06 07:00:00` in Asia/Shanghai unless the source explicitly states another timezone.
- Preserve minute and second precision when provided; do not add false precision when absent.
- If removal is confirmed but its time cannot be traced, write `已下架`, leave `下架时间` empty, and report the missing evidence.
- Do not use the lookup date, research date, last update date, or a shared batch date as the removal time.

## Identity and Region

- Match by Apple numeric ID or Android package ID before matching by title.
- Treat title changes under the same stable ID as the same app.
- Do not merge similarly named apps with different stable IDs.
- Keep storefront/country consistent across store, Qimai, and Diandian checks. Regional absence does not prove global removal.

## iTunes Lookup Fields

When available, use these values as enrichment inputs:

- `trackId`, `bundleId`, `trackName`
- `description`
- `primaryGenreName`
- `currentVersionReleaseDate`
- `userRatingCount`
- `artworkUrl512`
- `screenshotUrls`

Validate asset URLs and app identity before downloading or uploading them.
